let visited;
let countries;
const mappa = new Mappa('Leaflet');
let visitmap;
let canvas;

let data = [];

const options = {
  lat: 0,
  lng: 0,
  zoom: 1.5,
  style: 'http://{s}.tile.osm.org/{z}/{x}/{y}.png'
};

function preload() {
  visited = loadTable('../static/data/visited.csv', 'header');
  
  countries = loadJSON('../static/data/places.json');
}

function setup() {
  canvas = createCanvas(window.outerWidth, 400);
  visitmap = mappa.tileMap(options);
  visitmap.overlay(canvas);
  
  for (let row of visited.rows) {
    let coords = countries[row.get('id')];
    let latitude = coords[0]
    let longitude = coords[1]
    data.push({latitude,longitude});
  }

  console.log(data);

  // console.log(countries);
  //console.log(youtubeData);
}

function draw() {
  clear();
  for (let country of data) {
    const pix = visitmap.latLngToPixel(country.latitude, country.longitude);
    fill(255, 0, 200, 100);
    const zoom = visitmap.zoom();
    const scl = pow(2, zoom); // * sin(frameCount * 0.1);
    ellipse(pix.x, pix.y, 3 * scl);
  }
}