import React from 'react';
import { render, screen } from '@testing-library/react';
import TaskRouter from '../../../frontend/src/components/TaskRouter';

describe('TaskRouter Component', () => {
  test('renders task router panel', () => {
    render(<TaskRouter />);
    expect(screen.getByText(/Task Log/i)).toBeInTheDocument();
  });
});
