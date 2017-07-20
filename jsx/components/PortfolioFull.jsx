import React from 'react';
import ImageGallery from 'react-image-gallery';

class PortfolioFull extends React.Component {

	constructor(props) {
        super(props);
        this.displayName = 'PortfolioFull';
        this.state = {
        	nombre:'',
        	descripcion:'',
        	imagenes : []
        };
    }
    componentWillMount() {
    	//debugger;
		const self =this;
		const seleccionado = this.props.seleccionado;
		const url = '/api/projectoimagenro/'+seleccionado;
	    Promise.resolve($.get(url))
	    .then((result)=>{
	    	//debugger;
	    	self.setState({
	    		nombre : result.nombre,
	    		descripcion : result.descripcion,
	    		imagenes : result.imagenes		
	    	})
	    })
	    .catch((e)=>{
	    	console.log(e);
	    }); 
	}
    render() {
        return(
        		<div className='contenedor-modal' >
        			<div className='contenedor-gallery center'>
	        			<ImageGallery 
	        				items = {this.state.imagenes}
	        				ref={i => this._imageGallery = i}
	        				lazyLoad = {true}
	        			/>
        			</div>
						<div className="bodyfull">
	        			
	        				<h2>{
	        						this.state.nombre
	        					}
	        				</h2>
	        			<div dangerouslySetInnerHTML={{__html: this.state.descripcion}}/>
	        			
        			

        			</div>	
        		</div>
        	)
    }
}



export default PortfolioFull;
