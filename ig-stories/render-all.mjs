// Render all IG story HTML files in this folder to JPGs.
// Usage: node render-all.mjs        — renders all stories
//        node render-all.mjs 01-poll — renders one story
import { chromium } from 'playwright';
import { fileURLToPath } from 'url';
import { readdirSync, statSync } from 'fs';
import path from 'path';

const __dirname = path.dirname(fileURLToPath(import.meta.url));

const only = process.argv[2];
const folders = readdirSync(__dirname)
  .filter(name => statSync(path.join(__dirname, name)).isDirectory())
  .filter(name => !only || name === only);

const browser = await chromium.launch({
  executablePath: '/opt/pw-browsers/chromium-1194/chrome-linux/chrome',
  args: ['--no-sandbox'],
});

for (const folder of folders) {
  const htmlPath = path.join(__dirname, folder, 'index.html');
  const outPath = path.join(__dirname, folder, 'render.jpg');
  try {
    statSync(htmlPath);
  } catch {
    console.log('Skipping', folder, '(no index.html)');
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
  console.log('✓', folder, '→', outPath);
}

await browser.close();
