import logo from './logo.svg';
import './App.css';
import AutoComplete from './components/auto-complete';
import { useCallback, useState } from 'react';

function App() {
    const refreshSuggestions = useCallback((text) => {
        const lowerText = text.toLowerCase();
        const newSuggestions = allSuggestions.filter(suggestion => suggestion.indexOf(lowerText) !== -1);
        console.log(`new suggestions are ${newSuggestions}`);
        setSuggestions(newSuggestions);
    }, []);
    const allSuggestions = ["hello", "how are you", "bye", "good morning", "good evening", "good night", "whatsapp", "ssupp"];
    const [suggestions, setSuggestions] = useState(allSuggestions);
    return (
        <div className="App">
            <header className="App-header">
                <AutoComplete onTextChange={refreshSuggestions} suggestions={suggestions}/>
            </header>
        </div>
    );
}

export default App;
