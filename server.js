const express = require('express')
const fs = require('fs');


const app = express()
const port = 3000
var server = app.listen(port);

app.use(express.static('public'));

let rawPortfolioData = fs.readFileSync('public/portfolio/portfolio.json');  
let portfolio = JSON.parse(rawPortfolioData);

let rawAboutMeData = fs.readFileSync('public/about/about.json');
let about = JSON.parse(rawAboutMeData);

let rawBlogsData = fs.readFileSync('public/blogs/blogs.json');
let blogs = JSON.parse(rawBlogsData);

let rawWorksData = fs.readFileSync('public/works/works.json');
let works = JSON.parse(rawWorksData);

let rawGalleryImagesData = fs.readFileSync('public/imgs_from_galleries/imgs_from_galleries.json');
let galleryImages = JSON.parse(rawGalleryImagesData);

let rawResumeData = fs.readFileSync('public/resume/resume.json');
let resume = JSON.parse(rawResumeData);


app.get('/', (req, res) => res.json(portfolio));
app.get('/portfolio', (req, res) => res.json(portfolio));
app.get('/portfolio.json', (req, res) => res.json(portfolio));

app.get('/about', (req, res) => res.json(about));
app.get('/about.json', (req, res) => res.json(about));

app.get('/resume', (req, res) => res.json(resume));
app.get('/resume.json', (req, res) => res.json(resume));
app.get('/resume.pdf', (req, res) => res.json(resume));

app.get('/works', (req, res) => res.json(works));
app.get('/work', (req, res) => res.json(works));
app.get('/works.json', (req, res) => res.json(works));

app.get('/blogs', (req, res) => res.json(blogs));
app.get('/blog', (req, res) => res.json(blogs));
app.get('/blogs.json', (req, res) => res.json(blogs));

app.get('/imgs_from_galleries', (req, res) => res.json(galleryImages));
app.get('/images', (req, res) => res.json(galleryImages));
app.get('/imgs_from_galleries.json', (req, res) => res.json(galleryImages));



if (server) {
    console.log("server running at port: " + port);
}