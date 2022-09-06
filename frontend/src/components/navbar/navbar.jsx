import './navbar.css';
import { Component } from 'react';
import { Link } from 'react-router-dom'
import trasnlation from '../../constants/translations.json'
export default class Navbar extends Component {
    constructor(props) {
        super(props);
        this.state = {

        }
    }
    render() {
        return (
        <div className="navbar">
            <div>
                <Link className="navbar__title" to='/'> {trasnlation.navBar.homePage.en} </Link>
                <Link className="navbar__title" to='/search'> {trasnlation.navBar.searchRiskFactors.en} </Link>
            </div>
            <div>
                <Link className="navbar__title" to='/privacy'> {trasnlation.navBar.privacyPolicy.en} </Link>
                <a className="navbar__title" href={trasnlation.navBar.contact.link.en} > {trasnlation.navBar.contact.title.en} </a>
            </div>
        </div>
        );
  }
};