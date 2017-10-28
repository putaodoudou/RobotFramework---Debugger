import * as React from 'react';
import './StartTestSuite.css';

interface Props {
  name: string;
}

interface State {
  name: string;
}

/* tslint:disable:no-any */
/* tslint:disable:no-console */
class StartTestSuite extends React.Component<Props> {
  public state: State = {
    name: ''
  };

  constructor(props: Props) {
    super(props);
    this.handleNameChange = this.handleNameChange.bind(this);
    this.handleNameSubmit = this.handleNameSubmit.bind(this);
  }

  handleNameChange(event: any): void {
    this.setState({ name: event.target.value });
  }

  handleNameSubmit(): void {
    console.log('StartTestSuite.handleNameSubmit initiated');
    
    fetch(`http://localhost:5000/start-test-suite/${this.state.name}`)
      .then(response => {
        console.log(response);
      })
      .catch(error => {
        console.log(error);
      });
  }

  render() {
    return (
      <form>
        <label>
          Test Suite Name:
          <input type="text" value={this.state.name} onChange={e => this.handleNameChange(e)} />
        </label>
        <input type="button" value="Start Test" onClick={this.handleNameSubmit} />
      </form>
    );
  }
}

export default StartTestSuite;