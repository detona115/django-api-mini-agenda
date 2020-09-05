import React, {Component} from 'react';
import axios from 'axios';

class App extends Component{
  constructor(props){
    super(props);
    this.state = { agendas: []};
  }

  componentDidMount(){
    this.getAgendas();
  }

  getAgendas(){
    axios
      .get('http://127.0.0.1:8000/api/v1/')
      .then(res => {
        this.setState({ agendas: res.data});
      })
      .catch(err => {
        console.log(err);
      });
  }

  render(){
    return(
      <div>
        {
          this.state.agendas.map(item =>(
            <div key={item.id}>
              <h1>{item.subject}</h1>
              <p>{item.date}</p>
              <p>{item.person}</p>
              <p>{item.priority}</p>
              <p>{item.place}</p>
              <p>{item.email}</p>
              <p>{item.contact}</p>
            </div>
          ))
        }
      </div>
    );
  }
}

export default App;
