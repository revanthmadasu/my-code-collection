const fruits = [
    {
        id: "mango",
        name: "Mango",
        fruitItems: [
            {
                image: "./assets/fruits/mango.jpeg",
                description: "Mango is a tropical fruit renowned for its sweet, juicy, and aromatic flesh. Belonging to the genus Mangifera, it is native to South Asia but is now grown in various tropical and subtropical regions worldwide."
            }
        ]
    }, 
    {
        id: "banana",
        name: "Banana",
        fruitItems: [
            {
                image: "./assets/fruits/banana.webp",
                description: "Banana is a popular tropical fruit known for its distinctive elongated shape, sweet taste, and creamy texture. Belonging to the genus Musa, it is native to Southeast Asia but is now grown in many warm and tropical regions around the world. "
            }
        ]
    },
    {
        id: "guava",
        name: "Guava",
        fruitItems: [
            {
                image: "./assets/fruits/guava.jpeg",
                description: "Guava is a tropical fruit with a unique flavor and aromatic fragrance. It belongs to the Myrtaceae family and is native to Central America, but it is now widely cultivated in tropical and subtropical regions around the world. "
            }
        ]
    },
    {
        id: "papaya",
        name: "Papaya",
        fruitItems: [
            {
                image: "./assets/fruits/papaya.jpeg",
                description: "Papaya is a tropical fruit renowned for its vibrant color, soft texture, and sweet, musky flavor. It belongs to the Caricaceae family and is native to Central America and Mexico. Today, papaya is grown in various warm regions worldwide, including parts of Asia, Africa, and the Caribbean."
            }
        ]
    },
    {
        id: "jackfruit",
        name: "Jackfruit",
        fruitItems: [
            {
                image: "./assets/fruits/jackfruit.webp",
                description: "Jackfruit is a large tropical fruit known for its immense size, distinctive appearance, and unique flavor. It belongs to the Moraceae family and is native to South Asia, primarily found in countries like India, Bangladesh, and Sri Lanka. Jackfruit trees are large, evergreen trees with glossy green leaves and can bear multiple fruits simultaneously."
            }
        ]
    },
    {
        id: "orange",
        name: "Orange",
        fruitItems: [
            {
                image: "./assets/fruits/orange.jpeg",
                description: "Oranges are vibrant and refreshing citrus fruits, widely recognized for their bright color, juicy pulp, and zesty flavor. Belonging to the Rutaceae family, oranges are believed to have originated in Southeast Asia and are now extensively grown in warm regions across the globe."
            }
        ]
    },
    {
        id: "lemon",
        name: "Lemon",
        fruitItems: [
            {
                image: "./assets/fruits/lemon.webp",
                description: "Lemons are bright and tangy citrus fruits, renowned for their refreshing flavor and numerous culinary and medicinal uses. Belonging to the Rutaceae family, lemons are thought to have originated in Southeast Asia and are now grown in various subtropical and Mediterranean regions."
            }
        ]
    },
    {
        id: "lime",
        name: "Lime",
        fruitItems: [
            {
                image: "./assets/fruits/lime.webp",
                description: "Lime is a small, green citrus fruit known for its tart and tangy flavor. Belonging to the Rutaceae family, limes are native to Southeast Asia but are now cultivated in many tropical and subtropical regions around the world."
            }
        ]
    },
    {
        id: "sweet_lime",
        name: "Sweet Lime",
        fruitItems: [
            {
                image: "./assets/fruits/sweeu_lime.jpeg",
                description: "Sweet lime, also known as sweet lemon or mitha nimbu, is a citrus fruit belonging to the Rutaceae family. It is a hybrid between a mandarin and a lemon, resulting in a fruit with a unique and mild flavor profile. Sweet limes are commonly grown in subtropical and tropical regions."
            }
        ]
    },
    {
        id: "peach",
        name: "Peach",
        fruitItems: [
            {
                image: "./assets/fruits/peach.jpeg",
                description: "Peach is a delicious and fragrant fruit known for its sweet and juicy flesh. Belonging to the genus Prunus, peaches are part of the Rosaceae family and are believed to have originated in China. Today, they are grown in various temperate regions around the world."
            }
        ]
    },
    {
        id: "plum",
        name: "Plum",
        fruitItems: [
            {
                image: "./assets/fruits/plum.jpeg",
                description: "Plum is a juicy and flavorful fruit known for its rich, sweet-tart taste and vibrant colors. Belonging to the genus Prunus, plums are part of the Rosaceae family and are native to various regions across Europe, Asia, and North America. They are now cultivated in many temperate regions around the world."
            }
        ]
    },
    {
        id: "apricot",
        name: "Apricot",
        fruitItems: [
            {
                image: "./assets/fruits/apricot.jpeg",
                description: "Apricot is a small, golden-orange fruit known for its sweet and slightly tart flavor. Belonging to the Prunus genus, apricots are part of the Rosaceae family and are believed to have originated in China. They are now widely grown in temperate regions around the world."
            }
        ]
    },
    {
        id: "cherry",
        name: "Cherry",
        fruitItems: [
            {
                image: "./assets/fruits/cherry.jpeg",
                description: "Cherry is a small, vibrant fruit known for its sweet and tart flavor. Belonging to the genus Prunus, cherries are part of the Rosaceae family and are native to temperate regions in the Northern Hemisphere. They are cultivated in many countries around the world, with various cherry varieties available."
            }
        ]
    },
    {
        id: "strawberry",
        name: "Strawberry",
        fruitItems: [
            {
                image: "./assets/fruits/strawberry.jpeg",
                description: "Strawberry is a luscious and juicy fruit known for its sweet and slightly tangy flavor. Belonging to the Fragaria genus, strawberries are part of the Rosaceae family and are native to temperate regions in both the Northern and Southern Hemispheres. They are now widely cultivated around the world, making them one of the most popular and beloved berries."
            }
        ]
    }
];

const getFruitHtml = (fruits) => {
    fruits.map(fruit => {
        let html = `
        <div id="${fruit.id}" class="fruit-description-item">
            <h4 class="primary">${fruit.name}</h4>
            ${
                fruit.fruitItems.map(fItem => {
                return `
            <p>${fItem.description}</p>
            <img class="fruit-image image-medium" src="${fItem.image}">
                    `;
                }).join("")
            }
        <div>
        `;
        // fruit.fruitItems.map(fItem => {
        //     return `
        //         <p>${fItem.description}</p>
        //         <img class="fruit-image image-medium" src="${fItem.image}>
        //         `;
        // }).join("");
        console.log(html);
        return html;
    });
};

getFruitHtml(fruits);