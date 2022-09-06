import './search-page.css';
import { Component } from 'react';
import SearchResultSummary from '../search-result-summary/search-result-summary'
import SearchBar from '../searchbar/searchbar'
import SelectSectors from '../sector-select/sector-select'
import { BallTriangle } from 'react-loader-spinner';
import trasnlation from '../../constants/translations.json'
import Logo from '../logo/logo'
export default class SearchPage extends Component {
    constructor(props) {
        super(props);
        this.state = { loading: false, sectors: [], num_results: 20, show_error: false, theres_no_results: false}
    }

    toggleLoader = () => {
        this.setState({loading: !this.state.loading})
    }

    showErrorMessage = (status) => {
        this.setState({show_error: status})
    }

    showNoResultMessage = (status) => {
        this.setState({theres_no_results: status})
    }

    updateResults = (data) => {
        this.setState({results: data})
    }

    updateSearchWord = (searched_word) => {
        this.setState({searched_word: searched_word})
    }

    updateSectors = (sector) => {
        let list = this.state.sectors
        if (list.includes(sector)) {
            // if sector was deselected, remove it from the list of sectors
            list = list.filter(existingSector => existingSector !== sector)
        } else {
            // if sector was selected, add it to the list of sectors
            list.push(sector)
        }
        this.setState({sectors: list})
    }

    updateResultNumber = (number) => {
        this.setState({num_results: number})
    }

    errorMessage = () => {
        return (<p className="searchpage__search-result-for"> {trasnlation.searchPage.errorMessage.en}</p>)
    }

    noResultMessage = () => {
        return (<p className="searchpage__search-result-for"> {trasnlation.searchPage.noResult.en}</p>)
    }
    render() {
        const searchResults = [];
        for (const rank in this.state.results) {
            searchResults.push(
            <SearchResultSummary 
                key={rank}
                company_name={this.state.results[rank]["company details"].company_name} 
                header={this.state.results[rank]["risk factor"].header}
                text={this.state.results[rank]["risk factor"].text}
                date={this.state.results[rank]["filing details"].date_of_filing}
                link={this.state.results[rank]["filing details"].link_to_filing}  
                ticker={this.state.results[rank]["company details"].ticker} 
                // sector={this.state.result[rank]["company details"].sector}
            />
            )
        }
        return (
            <div className="searchpage__container">
                <div className="searchpage__left-col">
                    <Logo />
                    <h3 className="searchpage__risk-factor-title"> {trasnlation.searchPage.title.en}</h3>
                    <SearchBar 
                        mountLoader={this.toggleLoader}
                        showResult={this.updateResults} 
                        updateSearchWord={this.updateSearchWord}
                        showError={this.showErrorMessage}
                        showNoResult={this.showNoResultMessage}
                        sectors={this.state.sectors}
                        num_results={this.state.num_results}
                    />
                    {/* check if error message should appear, then if there is a result to show and finally show the result */}
                    {this.state.show_error ? this.errorMessage() :
                        this.state.theres_no_results?  this.noResultMessage() : 
                            this.state.searched_word && <p className="searchpage__search-result-for"> {trasnlation.searchPage.searchResultFor.en} <u>{this.state.searched_word}</u>...</p>
                    }
                    
                    {this.state.loading ? 
                        <div className="searchpage__loading-spinner">
                            <BallTriangle color='grey' ariaLabel='loading'/>
                        </div> 
                        : searchResults
                    }
                </div>
                <div className="searchpage__right-col">
                    <SelectSectors updateSectors={this.updateSectors} updateResultNumber={this.updateResultNumber} currentResultNumber={this.state.num_results}/>
                </div>
                
                        
            </div>
            
        )
    }
}