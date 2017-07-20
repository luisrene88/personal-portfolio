import PortfolioSmall from './PortfolioSmall.jsx';
import React from 'react';

class ListPortfolio extends React.Component {
    constructor(props) {
        super(props);
        this.displayName = 'ListPortfolio';
    }
    eachItem(item, i) {
        //console.log(item.picture);
        //debugger;
        const imgurl = item.imagenes.length > 0 ? item.imagenes[0].image : 'http://placehold.it/640x480';
        return (<PortfolioSmall
            key = {item.id}
            _id={item.id}
            index = {item.index}
            image={imgurl}
            name = {item.nombre}
        />);
    }
    render() {
        return <div className="ed-container justify">
        	{
        		this.props.datos.map(this.eachItem)
        	}
        </div>;
    }
}

export default ListPortfolio;
