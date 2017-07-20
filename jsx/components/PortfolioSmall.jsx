import  React from 'react';
import PortfolioFull from './PortfolioFull.jsx';
import {ModalContainer, ModalDialog} from 'react-modal-dialog';

class PortfolioSmall extends React.Component {
	constructor(props) {
        super(props);
        this.displayName = 'PortfolioSmall';
        this.state={
        	isopen:false
        };
	
    }
    open(){
    	
        this.setState({
    		isopen:true
    	});
    }
    close(){
    	this.setState({
    		isopen:false
    	});	
    }
    render() {
        return (
        	<div onClick={this.open.bind(this)} className="elemento ed-item tablet-30 web-25 portfoliosmall">
        	<div className="elemento__imagen">
        		<img className="center" src={this.props.image}/>
        	</div>
        	<div className="main-center">
        		<span className='elemento__titulo'>{this.props.name}</span>
			</div>
            {
				    this.state.isopen &&
                    <ModalContainer onClose={this.close.bind(this)}>
                      <ModalDialog onClose={this.close.bind(this)}>
                        <PortfolioFull
                        seleccionado = {this.props._id}
                        />
                      </ModalDialog>
                    </ModalContainer>
                
			}
            
        </div>
        );
    }
}

export default PortfolioSmall;
