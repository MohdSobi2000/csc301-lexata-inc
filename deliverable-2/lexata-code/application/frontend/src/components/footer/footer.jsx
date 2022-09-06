import './footer.css';
import { Component } from 'react';
import translation from "../../constants/translations.json"
export default class Footer extends Component {
    constructor(props) {
        super(props);
        this.state = {

        }
    }
    render() {
        return (
        <div className="footer__container">
            <div className="footer__section">
                <label> {translation.footer.section1.subtitle1.en}</label>
                <label> {translation.footer.section1.subtitle2.en}</label> 
            </div>

            <div className="footer__section">
                <p> {translation.footer.section2.subtitle1.en}</p>
            </div>

            <div className="footer__section">
                <label> {translation.footer.section3.subtitle1.en}</label>
                <label> {translation.footer.section3.subtitle2.en}</label>
            </div>
        </div>
        );
  }
};