import './privacy-policy.css';
import Logo from '../logo/logo'
import translation from '../../constants/translations.json'
export default function PrivacyPolicy(props) {
    return (
            <div className="privacy-policy__container">
                <Logo />
                <h3 className="privacy-policy__title"> {translation.privacyPolicy.title.en} </h3>

                <div className="privacy-policy__par">
                    <p className="privacy-policy__par-title"> {translation.privacyPolicy.par1.title.en} </p>
                    <p className="privacy-policy__par-text"> {translation.privacyPolicy.par1.subtitle1.en} </p>
                </div>

                <div className="privacy-policy__par">
                    <p className="privacy-policy__par-title"> {translation.privacyPolicy.par2.title.en} </p>
                    <p className="privacy-policy__par-text"> {translation.privacyPolicy.par2.subtitle1.en} </p>
                    <p className="privacy-policy__par-text"> {translation.privacyPolicy.par2.subtitle2.en} </p>
                </div>

                <div className="privacy-policy__par">
                    <p className="privacy-policy__par-title"> {translation.privacyPolicy.par3.title.en} </p>
                    <p className="privacy-policy__par-text"> {translation.privacyPolicy.par3.subtitle1.en} </p>
                </div>
            </div>
    )
}