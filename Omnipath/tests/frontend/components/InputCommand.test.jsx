import React from 'react';
import { render, fireEvent, screen } from '@testing-library/react';
import InputCommand from '../../../frontend/src/components/InputCommand';

describe('InputCommand Component', () => {
  test('renders input and button', () => {
    render(<InputCommand />);
    expect(screen.getByPlaceholderText(/type a command/i)).toBeInTheDocument();
    expect(screen.getByRole('button')).toBeInTheDocument();
  });

  test('handles user input', () => {
    render(<InputCommand />);
    const input = screen.getByPlaceholderText(/type a command/i);
    fireEvent.change(input, { target: { value: 'run diagnostics' } });
    expect(input.value).toBe('run diagnostics');
  });
});
