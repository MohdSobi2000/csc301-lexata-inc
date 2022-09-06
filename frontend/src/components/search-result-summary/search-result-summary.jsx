import './search-result-summary.css';
import { useState } from 'react';
import translation from '../../constants/translations.json'
export default function SearchResultSummary(props) {
    const ReadMore = (text) => {
        const [isReadMore, setIsReadMore] = useState(true);
        const toggleReadMore = () => {
          setIsReadMore(!isReadMore);
        };
        return (
          <p className="search-result-summary__text">
            {isReadMore ? text.slice(0, 250) : text}
            <span onClick={toggleReadMore} className="search-result-summary__readmore">
              {isReadMore ? "Read More... " : " Show Less"}
            </span>
          </p>
        );
      };

    return (
            <div className="search-result-summary__container">
                <div className="search-result-summary__seperator"></div>
                <div className="search-result-summary__first-line">
                    <p className="search-result-summary__company-name"> {props.company_name} </p>
                    <div className="search-result-summary__details">
                        <p className="search-result-summary__details-info"> {props.date} </p>
                        {/* <span className="search-result-summary__details-seperator"> - </span> */}
                        <p className="search-result-summary__details-info"> {translation.searchResultSummary.form.en}</p>
                        {/* <span className="search-result-summary__details-seperator"> - </span> */}
                        <a className="search-result-summary__details-info" href={props.link} target="_blank" rel='noreferrer'> {props.ticker} </a>
                        
                    </div>
                </div>
                {/* <p className="search-result-summary__section"> {props.sector} </p> */}
                
                {ReadMore(props.header.concat(props.text))}
            </div>
    )
}