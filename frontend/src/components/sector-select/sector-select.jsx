import './sector-select.css';
import { Component } from 'react';
import translation from '../../constants/translations.json'
import sectors from '../../constants/sectors.json'
export default class SelectSectors extends Component {
    constructor(props) {
        super(props);
        this.state = {}
    }

    render() {
        // store list of all the sectors
        const list_of_sectors = Object.keys(sectors)
    
        return (
                <div className="selectsectors__container">
                    <h3 className="selectsectors__title"> {translation.filterSection.title.en} </h3>
                    <p className="selectsectors__subtitle"> {translation.filterSection.sectors.en} </p>
                    <form className="selectsectors__menu">
                        {list_of_sectors.map((sector) => 
                            <div className="selectsectors__checkbox-container" key={`${sector} line`}> 
                                <input 
                                    className="selectsectors__checkbox" 
                                    type="checkbox" 
                                    name={sector} 
                                    id={sector}
                                    value={sector}
                                    onChange={() => this.props.updateSectors(sector)}
                                    key={sector}
                                ></input>
                                <label className="selectsectors__checkbox-label" htmlFor={sector} key={`${sector} label`}>{sectors[sector].en}</label>
                            </div>
                     )}
                    </form>
                    <p className="selectsectors__subtitle"> {translation.filterSection.numberOfResults.en} </p>
                    <form className="selectsectors__number-of-results">
                    <select className="selectsectors__number-of-results-dropdown" name="num_results" id="num_results" onChange={(e) => this.props.updateResultNumber(e.target.value)}>
                        {Array.from(Array(20), (_, index) => index + 1).map((number) => number !==this.props.currentResultNumber ? 
                                                                        <option value={number}>{number}</option> : 
                                                                        <option selected value={number}> {number}</option>)}
                    </select>
                    </form>
                </div>
                
            )
        }
}
            