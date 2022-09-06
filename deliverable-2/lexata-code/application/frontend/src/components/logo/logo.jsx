import './logo.css'
import logo from '../../assets/lexatalogo.png'
import { Link } from 'react-router-dom'
import trasnlation from '../../constants/translations.json'
export default function Logo(props) {
    return (
        <div className="logo__container">
                <Link className="logo__link" to={`/`}>
                    <img 
                        className="logo__img"
                        src={logo} 
                        alt="lexata Logo" 
                    />
                </Link>
                <p className="logo__slogan"> {trasnlation.logo.slogan.en} </p>
        </div>
    );
  }