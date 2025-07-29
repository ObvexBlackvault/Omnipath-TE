import React from 'react';
import { render, screen } from '@testing-library/react';
import App from '../../frontend/src/App';

describe('App Component', () => {
  test('renders the command input', () => {
    render(<App />);
    expect(screen.getByPlaceholderText(/Enter command/i)).toBeInTheDocument();
  });

  test('renders core components', () => {
    render(<App />);
    expect(screen.getByText(/Agent Status/i)).toBeInTheDocument();
    expect(screen.getByText(/Task Logs/i)).toBeInTheDocument();
  });
});
