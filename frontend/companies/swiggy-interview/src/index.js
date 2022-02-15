// import "./styles.css";

let buttons = [1, 2, 3, 4, 5];

function render() {
  let htmlCode = "";
  buttons.forEach((button, index) => {
    htmlCode += `<button onclick="buttons = buttons.slice(0,${index}).concat(${[button,...buttons.slice(index)]}); render();">${button}</button>`;
  });
  document.getElementById("app").innerHTML = htmlCode;
}

render();
const parentNode = document.getElementById("root");
const childNode = document.getElementById("a-inner");

function getNextRightNode(parentNode, childNode) {
    // const children = parentNode.children;
    const children = childNode.parentNode.children;
    let childVisited = false;
    let i = 0;
    for (i=0; i<children.length; ++i) {
        child = children[i];
        if (child.id === childNode.id) {
            childVisited = true;
            break;
        }
    }
    return i+1 >= children.length ? 'No Right child' : children[i+1];
}

console.log(getNextRightNode(parentNode, childNode));