// Constant variables which should be accessible dependent on their environment
// Solution inspired by:
// https://a-carreras-c.medium.com/development-and-production-variables-for-react-apps-c04af8b430a5

/**
 * Environment variables for the development environment.
 */
const dev = {
  url: {
    API_URL: "http://127.0.0.1:4000"
  }
};

/**
* Environment variables for the production environment.
*/
const prod = {
  url: {
    // TODO change when deployed to a remote server.
    API_URL: "http://127.0.0.1:4000"
  }
};

export const config = process.env.NODE_ENV === "development" ? dev : prod;
