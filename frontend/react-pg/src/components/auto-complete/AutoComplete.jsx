import { useCallback, useState, useMemo } from "react"
import "./AutoComplete.css";
export const AutoComplete = ({onTextChange, suggestions}) => {
    const onTextInput = useCallback((event) => {
        console.log(event.target.value);
        onTextChange(event.target.value);
    }, [onTextChange]);
    const suggestionsTags = useMemo(() => {
        return suggestions.map(suggestion => <li className="list-group-item">{suggestion}</li>);
    }, [suggestions]);
    return <>    
        <div className="auto-complete position-relative d-inline-flex">
            <input type="text" onKeyDown={onTextInput} />
            <div className="suggestions d-inline-block position-absolute">
                <ul className="list-group suggestions-list">
                    {suggestionsTags}
                </ul>
            </div>
        </div>
    </>
};