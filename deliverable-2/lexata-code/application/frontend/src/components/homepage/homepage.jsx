import './homepage.css';
import translation from '../../constants/translations.json'
import Logo from '../logo/logo'
import pic1 from '../../assets/homepagepic.jpg'
import pic2 from '../../assets/homepagepic2.jpg'
import pic3 from '../../assets/homepagepic3.jpg'
export default function HomePage(props) {
    return (
        <div className="homepage__container">
            <Logo />
            <div className="homepage__section-odd">
                <div className="homepage__section-odd-left">
                    <h3 className="homepage__section-title"> {translation.homepage.firstSection.title.en} </h3>
                    <label className="homepage__section-subtitle"> {translation.homepage.firstSection.subtitle1.en}</label>
                    <label className="homepage__section-subtitle"> {translation.homepage.firstSection.subtitle2.en}</label>
                    <label className="homepage__section-subtitle"> {translation.homepage.firstSection.subtitle3.en}</label>
                </div>
                <div className="homepage__section-odd-right">
                    <img 
                        className="homepage__img1"
                        src={pic1} 
                        alt="homepagePic1" 
                    />
                </div>
            </div>

            <div className="homepage__section-even">
                <div className="homepage__section-even-left">
                    <img 
                        className="homepage__img2"
                        src={pic2} 
                        alt="homepagePic2" 
                    />
                </div>
                <div className="homepage__section-even-right">
                    <h3 className="homepage__section-title left_title"> {translation.homepage.secondSection.title.en} </h3>
                    <p className="homepage__section-subtitle"> {translation.homepage.secondSection.subtitle1.en} </p>
                    <ul className="homepage__ul">
                        <li className="homepage__section-subtitle"> {translation.homepage.secondSection.list.row1.en} </li>
                        <li className="homepage__section-subtitle"> {translation.homepage.secondSection.list.row2.en} </li>
                        <li className="homepage__section-subtitle"> {translation.homepage.secondSection.list.row3.en} </li>
                        <li className="homepage__section-subtitle"> {translation.homepage.secondSection.list.row4.en}</li>
                        <li className="homepage__section-subtitle"> {translation.homepage.secondSection.list.row5.en} </li>
                        <li className="homepage__section-subtitle"> {translation.homepage.secondSection.list.row6.en} </li>
                    </ul>
                    <label className="homepage__section-subtitle"> {translation.homepage.secondSection.subtitle2.en}</label>
                    <label className="homepage__section-subtitle"> {translation.homepage.secondSection.subtitle3.en} </label>
                </div>
            </div>

            <div className="homepage__section-odd">
                <div className="homepage__section-odd-left">
                    <h3 className="homepage__section-title"> {translation.homepage.thirdSection.title.en} </h3>
                    <label className="homepage__section-subtitle"> {translation.homepage.thirdSection.subtitle1.en}</label>
                    <label className="homepage__section-subtitle"> {translation.homepage.thirdSection.subtitle2.en}</label>
                    <br></br>
                    <label className="homepage__section-subtitle"> {translation.homepage.thirdSection.subtitle3.en} </label>
                    <label className="homepage__section-subtitle"> {translation.homepage.thirdSection.subtitle4.en}</label>
                    <label className="homepage__section-subtitle"> {translation.homepage.thirdSection.subtitle5.en}</label>
                    <label className="homepage__section-subtitle"> {translation.homepage.thirdSection.subtitle6.en}</label>
                    <label className="homepage__section-subtitle"> {translation.homepage.thirdSection.subtitle7.en} </label>
                    <a href={translation.homepage.thirdSection.linkedinLink.en}> {translation.homepage.thirdSection.linkedin.en}</a>
                </div>
                <div className="homepage__section-odd-right">
                    <img 
                        className="homepage__img1"
                        src={pic3} 
                        alt="homepagePic1" 
                    />
                </div>
            </div>
            
        </div>
        
    )
}