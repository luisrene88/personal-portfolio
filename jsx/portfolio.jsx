import React from 'react';
import ReactDOM from 'react-dom';
import ListPortfolio from './components/ListPortfolio.jsx';

const styles = {
	padding : '15px'
}
const url ='/api/projectoro/';
Promise.resolve($.get(url))
.then((result)=>{
  ReactDOM.render(<ListPortfolio style={styles} datos={result} />, document.getElementById('container')); 
})
.catch((e)=>{
  console.log(e);
});

