import logo from './logo.svg';
import './App.css';
import AutoComplete from './components/auto-complete';
import { useCallback, useState } from 'react';
import ImageCarousel from './components/image-carousel';

function App() {
    const refreshSuggestions = useCallback((text) => {
        const lowerText = text.toLowerCase();
        const newSuggestions = allSuggestions.filter(suggestion => suggestion.indexOf(lowerText) !== -1);
        console.log(`new suggestions are ${newSuggestions}`);
        setSuggestions(newSuggestions);
    }, []);
    const allSuggestions = ["hello", "how are you", "bye", "good morning", "good evening", "good night", "whatsapp", "ssupp"];
    const [suggestions, setSuggestions] = useState(allSuggestions);

    const carouselItems = [
        {
            src: "assets/carousel/img_lights_wide.jpg",
            alt: "lights image",
        },
        {
          src: "assets/carousel/img_mountains_wide.jpg",
          alt: "mountains image",
        },
        {
          src: "assets/carousel/img_nature_wide.jpg",
          alt: "nature image",
        },
        {
          src: "assets/carousel/img_snow_wide.jpg",
          alt: "snow image",
        }
    ];
    return (
        <div className="App">
            <header className="App-header">
                {/* <AutoComplete onTextChange={refreshSuggestions} suggestions={suggestions}/> */}
                <ImageCarousel carouselItems={carouselItems}></ImageCarousel>
            </header>
        </div>
    );
}

export default App;
