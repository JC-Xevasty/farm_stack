import { Link } from "react-router-dom";

const ComponentOne = () => {
  return (
    <div className="component">
      <Link to="/">Home</Link>
      <Link to="/page-one">Page One</Link>
      <Link to="/page-two">Page Two</Link>
    </div>
  );
};
export default ComponentOne;
