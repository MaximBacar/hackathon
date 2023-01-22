import React from 'react'
import './Popup.css'
import { IconContext } from 'react-icons';
import * as AiIcons from "react-icons/ai";


function Popup(props) {
  return (props.trigger) ? (
    <div className='popup'>
        <div className='popupClose'>
        <IconContext.Provider value={{color: '#643B9F'} }>
                <AiIcons.AiOutlineClose id='popupClose' onClick={() => props.setTrigger(false)}/>
                { props.children }
                </IconContext.Provider>
                </div>

        <h3 className='loginHeader'>Login</h3>
        <br></br>
        <form method="post" className='inputTXT'>
  <label id='email' >
    Email  
    <input type="text" />
  </label>
  <br></br>
  <br></br>
  <label id='password'>
    Password 
    <input type="text"  />
  </label>

  

  <br></br>
  <br></br>

<button type='submit' id='loginBtn'> Login </button>


</form>
</div>
  ) : "";
}

export default Popup
