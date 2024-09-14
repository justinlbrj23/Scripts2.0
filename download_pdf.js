const puppeteer = require('puppeteer');
const fs = require('fs');
const path = require('path');

(async () => {
    const browser = await puppeteer.launch();
    const page = await browser.newPage();
    const url = 'https://www2.miamidadeclerk.gov/ocs/ImgViewerWF.aspx?QS=B6%2F9EwnZlIiih%2BgqiU8rawLJW%2Bj4E30XGWoN6L%2B82TlrI6ZKeBzZWEcmY6diy%2BbNvNcDVi9gRoQMfgufYMwZCEVFoj5IoptRFNP%2Fx1SkmMQh8tc3zUN%2BeUf8qEcBKoFwQ%2BVubIyJ5TdTYOjDh2WdRe5GivwuoM%2B407AC4fDr9HaHFltRzczAmIJEipn2YAV9EnzaAM3Ga2UKIuvtAVP1astLJBTnDma6BcNVz4zP%2FlcVP2f7qBpvOIoZQUGdgbl1VqTOAqy3I1pzYfjcq5SgH8Wi5EaIZwYsIGwDeSTTtDvzmkCZyVUIJA%3D%3D';
    
    await page.goto(url, { waitUntil: 'networkidle2' });

    // Click the download button
    await page.evaluate(() => {
        const downloadButton = document.querySelector("#viewer").shadowRoot.querySelector("#toolbar").shadowRoot.querySelector("#downloads").shadowRoot.querySelector("#download").shadowRoot.querySelector("#icon > cr-icon");
        downloadButton.click();
    });

    // Wait for the download to complete
    await page.waitForTimeout(10000); // Adjust the timeout as needed

    // Close the browser
    await browser.close();
})();