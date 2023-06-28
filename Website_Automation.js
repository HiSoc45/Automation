const fs = require('fs');
const path = require('path');

// Define the website structure
const websiteStructure = {
  index: {
    html: `
      <!DOCTYPE html>
      <html>
      <head>
        <title>My Business Website</title>
      </head>
      <body>
        <h1>Welcome to My Business</h1>
        <p>This is the homepage of my business website.</p>
      </body>
      </html>
    `,
    css: '',
    js: '',
  },
  about: {
    html: `
      <!DOCTYPE html>
      <html>
      <head>
        <title>About Us</title>
      </head>
      <body>
        <h1>About Us</h1>
        <p>Learn more about our business and our team.</p>
      </body>
      </html>
    `,
    css: '',
    js: '',
  },
  contact: {
    html: `
      <!DOCTYPE html>
      <html>
      <head>
        <title>Contact Us</title>
      </head>
      <body>
        <h1>Contact Us</h1>
        <p>Get in touch with us for any inquiries or feedback.</p>
      </body>
      </html>
    `,
    css: '',
    js: '',
  },
};

// Create website directories and files
function createWebsiteStructure() {
  Object.entries(websiteStructure).forEach(([page, content]) => {
    const pageDir = path.join(__dirname, page);
    fs.mkdirSync(pageDir);

    const htmlFile = path.join(pageDir, 'index.html');
    fs.writeFileSync(htmlFile, content.html);

    const cssFile = path.join(pageDir, 'style.css');
    fs.writeFileSync(cssFile, content.css);

    const jsFile = path.join(pageDir, 'script.js');
    fs.writeFileSync(jsFile, content.js);
  });
}

// Execute the website creation
createWebsiteStructure();
console.log('Website created successfully!');
