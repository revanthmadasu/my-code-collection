import { useMemo, useState } from "react";
import "./ImageCarousel.css";
export const ImageCarousel = ({carouselItems}) => {
    const [selectedItem, selectItem] = useState(carouselItems[0]);
    const carouselNavs = useMemo(() => {
        return carouselItems.map((item, index) => {
            return <span className={"carousel-nav-btn d-inline-block rounded-circle mx-1 " + (item == selectItem ? "active" : "")} onClick={() => selectItem(carouselItems[index])}></span>
        });
    }, [selectedItem, carouselItems]);
    return (
        <>
            <div className="carousel-container">
                <div className="image-container">
                    <img src={"../"+selectedItem.src} alt={selectedItem.alt} />
                </div>
                <div className="text-center">
                    {carouselNavs}
                </div>
            </div>
        </>
    );
}