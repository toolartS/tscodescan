import { chromium } from "playwright";

const url = process.argv[2];
if (!url) {
  console.error("URL missing");
  process.exit(1);
}

const browser = await chromium.launch({ headless: true });
const page = await browser.newPage();

await page.goto(url, { waitUntil: "networkidle" });

const text = await page.evaluate(() => {
  function visible(el) {
    const s = getComputedStyle(el);
    const r = el.getBoundingClientRect();
    return (
      s.display !== "none" &&
      s.visibility !== "hidden" &&
      s.opacity !== "0" &&
      r.width > 0 &&
      r.height > 0
    );
  }

  const walker = document.createTreeWalker(
    document.body,
    NodeFilter.SHOW_TEXT
  );

  let out = [];
  let n;
  while ((n = walker.nextNode())) {
    if (!n.textContent.trim()) continue;
    if (!visible(n.parentElement)) continue;
    out.push(n.textContent.trim());
  }

  return out.join("\n");
});

console.log(text);
await browser.close();
