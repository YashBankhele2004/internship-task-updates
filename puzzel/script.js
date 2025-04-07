// script.js
const puzzleGrid = document.getElementById('puzzle-grid');
const startButton = document.getElementById('start-button');
const movesCounter = document.getElementById('moves-counter');
const timerDisplay = document.getElementById('timer');
const imageUpload = document.getElementById('image-upload');
const difficultySelect = document.getElementById('difficulty');
const successMessage = document.getElementById('success-message');

let tiles = [];
let moves = 0;
let timer = 0;
let timerInterval;
let gridSize = 3;

// Load image and split into tiles
function loadImage(imageSrc) {
  const image = new Image();
  image.src = imageSrc;
  image.onload = () => {
    createTiles(image);
  };
}

// Create tiles from the image
function createTiles(image) {
  puzzleGrid.innerHTML = '';
  puzzleGrid.style.width = `${image.width}px`;
  puzzleGrid.style.height = `${image.height}px`;
  puzzleGrid.style.gridTemplateColumns = `repeat(${gridSize}, 1fr)`;
  puzzleGrid.style.gridTemplateRows = `repeat(${gridSize}, 1fr)`;

  const tileSize = image.width / gridSize;

  tiles = [];
  for (let i = 0; i < gridSize * gridSize; i++) {
    const tile = document.createElement('div');
    tile.classList.add('tile');
    tile.style.width = `${tileSize}px`;
    tile.style.height = `${tileSize}px`;
    tile.style.backgroundImage = `url(${image.src})`;
    tile.style.backgroundPosition = `-${(i % gridSize) * tileSize}px -${Math.floor(i / gridSize) * tileSize}px`;
    tile.dataset.index = i;
    tiles.push(tile);
    puzzleGrid.appendChild(tile);
  }
  shuffleTiles();
}

// Shuffle tiles
function shuffleTiles() {
  tiles.sort(() => Math.random() - 0.5);
  tiles.forEach((tile, index) => {
    puzzleGrid.appendChild(tile);
  });
  moves = 0;
  movesCounter.textContent = moves;
  startTimer();
}

// Drag and drop functionality
puzzleGrid.addEventListener('dragstart', (e) => {
  e.dataTransfer.setData('text/plain', e.target.dataset.index);
});

puzzleGrid.addEventListener('dragover', (e) => {
  e.preventDefault();
});

puzzleGrid.addEventListener('drop', (e) => {
  e.preventDefault();
  const fromIndex = e.dataTransfer.getData('text/plain');
  const toIndex = e.target.dataset.index;
  swapTiles(fromIndex, toIndex);
  checkPuzzleSolved();
});

function swapTiles(fromIndex, toIndex) {
  const fromTile = tiles[fromIndex];
  const toTile = tiles[toIndex];
  puzzleGrid.insertBefore(fromTile, toTile);
  tiles.splice(fromIndex, 1);
  tiles.splice(toIndex, 0, fromTile);
  moves++;
  movesCounter.textContent = moves;
}

// Check if the puzzle is solved
function checkPuzzleSolved() {
  const isSolved = tiles.every((tile, index) => tile.dataset.index == index);
  if (isSolved) {
    clearInterval(timerInterval);
    successMessage.classList.remove('hidden');
  }
}

// Timer functionality
function startTimer() {
  clearInterval(timerInterval);
  timer = 0;
  timerInterval = setInterval(() => {
    timer++;
    const minutes = Math.floor(timer / 60).toString().padStart(2, '0');
    const seconds = (timer % 60).toString().padStart(2, '0');
    timerDisplay.textContent = `${minutes}:${seconds}`;
  }, 1000);
}

// Start game
startButton.addEventListener('click', () => {
  successMessage.classList.add('hidden');
  gridSize = parseInt(difficultySelect.value);
  loadImage('default-image.jpg'); // Replace with a default image
});

// Upload custom image
imageUpload.addEventListener('change', (e) => {
  const file = e.target.files[0];
  if (file) {
    const reader = new FileReader();
    reader.onload = (event) => {
      loadImage(event.target.result);
    };
    reader.readAsDataURL(file);
  }
});