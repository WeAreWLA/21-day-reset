// Render all IG story HTML files to JPGs.
// Usage: node render-all.mjs               — renders every story (incl. Drafts/)
//        node render-all.mjs 05-recap      — renders one story by folder name
//        node render-all.mjs Drafts/01-poll — renders one draft by relative path
import { chromium } from 'playwright';
import { fileURLToPath } from 'url';
import { readdirSync, statSync } from 'fs';
import path from 'path';

const __dirname = path.dirname(fileURLToPath(import.meta.url));

// Collect story folders: top-level ones, plus anything inside Drafts/.
function collectStories() {
  const out = [];
  for (const name of readdirSync(__dirname)) {
    if (name === 'node_modules') continue;
    const full = path.join(__dirname, name);
    if (!statSync(full).isDirectory()) continue;
    if (name === 'Drafts') {
      for (const sub of readdirSync(full)) {
        const subFull = path.join(full, sub);
        if (statSync(subFull).isDirectory()) out.push(path.join('Drafts', sub));
      }
    } else {
      out.push(name);
    }
  }
  return out;
}

const only = process.argv[2];
const stories = collectStories().filter(s => !only || s === only);

const browser = await chromium.launch({
  executablePath: '/opt/pw-browsers/chromium-1194/chrome-linux/chrome',
  args: ['--no-sandbox'],
});

for (const story of stories) {
  const htmlPath = path.join(__dirname, story, 'index.html');
  const outPath = path.join(__dirname, story, 'render.jpg');
  try {
    statSync(htmlPath);
  } catch {
    console.log('Skipping', story, '(no index.html)');
    continue;
  }

  const context = await browser.newContext({
    viewport: { width: 1080, height: 1920 },
    deviceScaleFactor: 1,
  });
  const page = await context.newPage();
  await page.goto('file://' + htmlPath, { waitUntil: 'networkidle' });
  await page.evaluate(() => document.fonts.ready);
  await page.waitForTimeout(400);

  await page.screenshot({
    path: outPath,
    type: 'jpeg',
    quality: 92,
    clip: { x: 0, y: 0, width: 1080, height: 1920 },
  });
  await context.close();
  console.log('✓', story, '→', outPath);
}

await browser.close();
