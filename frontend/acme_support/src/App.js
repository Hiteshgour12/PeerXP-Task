// import logo from './logo.svg';
import './App.css';
import Header from './components/Header';
import Login from './components/Login';
import { HashRouter as Router, Route } from "react-router-dom";
import { Container } from "react-bootstrap";
function App() {
  return (
    <div className="App">
      {/* <Router> */}
        <Header/>
        {/* <Container>
          <main className="py-3">
          <Route path="/login" component={Login} />
          </main>
          
        </Container> */}
      {/* </Router> */}
    </div>
  );
}

export default App;
