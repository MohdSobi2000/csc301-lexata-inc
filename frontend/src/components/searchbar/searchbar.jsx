import './searchbar.css';
import { Component } from 'react';
import translation from '../../constants/translations.json'
export default class SearchBar extends Component {
    constructor(props) {
        super(props);
        this.state = {button_active: true}
    }
    search = () => {
        // disable search button to avoid multiple/rapid requests from the backend
        this.setState({button_active: !this.state.button_active})

        // show load spinner
        this.props.mountLoader()

        // remove the search input (which also result to search results to disapper)
        this.props.updateSearchWord('');

        // remove error message 
        this.props.showError(false)

        // remove no-Result Message
        this.props.showNoResult(false)

        // check if user has selected any sector to include it in api call
        let sectorIsSelected;
        this.props.sectors.length === 0 ? sectorIsSelected=false : sectorIsSelected=true;
    
        fetch(`/api/search?num_results=${this.props.num_results}${sectorIsSelected ? `&sectors=${this.props.sectors}` : ''}`, {
          method: 'POST',
          body: this.state.search_input,
        }).then(
          res => {
            if (res.ok) {
              return res.json();
            }
            return Promise.reject(res)
          }
        ).then(
          data => {
              // activate the search button 
              this.props.updateSearchWord(this.state.search_input)
              if (Object.keys(data).length === 0) {
                this.props.showNoResult(true)
              }
              this.props.showResult(data)
              this.props.mountLoader()
              this.setState({button_active: !this.state.button_active})
          }).catch(error => {
            console.log(error.status, error.statusText);

            this.props.showResult({})
            // hide load spinner

            this.props.mountLoader()
            // show error message

            this.props.showError(true)
            // activate the search button

            this.setState({button_active: !this.state.button_active})
          })
      }
  
    onInputchange = (event) => {
        this.setState({
          [event.target.name]: event.target.value
        });
      }
  
    render() {
        return (
            <div className="searchbar__container">
                <input 
                    type="text" 
                    className="searchbar__input"
                    name="search_input" 
                    value={this.state.search_input}
                    onChange={this.onInputchange}
                    id="searchbar" 
                    placeholder={translation.searchBar.placeholder.en} 
                />
                <button className="searchbar__btn" disabled={!this.state.button_active} onClick={this.search}> {translation.searchBar.buttonText.en} </button>
            </div>
        )
        }
}
            