import React, {useState} from 'react';
import * as FaIcons from "react-icons/fa";
import * as AiIcons from "react-icons/ai";
import { Link } from 'react-router-dom';
import { SidebarData } from './SidebarData';
import './Navbar.css'
import { IconContext } from 'react-icons';
import Popup from './Popup';


function Navbar() {
    const[sidebar, setSidebar] = useState(false)

    const showSidebar = () => setSidebar(!sidebar)

    const [buttonPopup, setButtonPopup] = useState(false);
  return (
    <>
    <IconContext.Provider value={{color: '#fff'}}>
        <div className='navbar'>
            <Link to ='#' className='menuBars'>
            <IconContext.Provider value={{color: '#643B9F'}}>
                <FaIcons.FaBars onClick={showSidebar}/>
                </IconContext.Provider>
            </Link>
        </div>
        <nav className={sidebar ? 'navMenu active' : 'navMenu'}>
            <ul className='navMenuItems' onClick={showSidebar}>
                <li className='navbarToggle'>
                   <Link to="#" className='menuBars'>
                    <AiIcons.AiOutlineClose/>
                   </Link>
                </li>
                {SidebarData.map((item,index) => {
                    return (
                        <li key={index} className={item.cName}>
                            <Link to={item.path}>
                                {item.icon}
                                <span>{item.title}</span>
                            </Link>
                        </li>
                    )
                })}
            </ul>
        </nav>
    </IconContext.Provider>
    
    <button className='login' onClick={() => setButtonPopup(true)}>Login</button>
    <button className='signUp'>Sign up</button>

    <Popup trigger ={buttonPopup} setTrigger = {setButtonPopup}>
    </Popup>

    </>
    )
}

export default Navbar
