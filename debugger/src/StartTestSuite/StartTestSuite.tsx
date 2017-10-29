import * as React from 'react';
import './StartTestSuite.css';

interface Props {
  name: string;
}

interface State {
  name: string;
  inProgress: boolean;
}

/* tslint:disable:no-any */
/* tslint:disable:no-console */
class StartTestSuite extends React.Component<Props> {
  public state: State = {
    name: '',
    inProgress: false,
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
    
    if (!this.state.inProgress) {
      fetch(`http://localhost:3001/${this.state.name}`)
        .then(res => res.text())
        .then(body => console.log(body));
    }
    // TODO: Set in progress to true
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