import React from 'react';
import { render, screen, waitFor } from '@testing-library/react';
import AgentPanel from '../../../frontend/src/components/AgentPanel';

describe('AgentPanel Component', () => {
  test('renders agent panel headers', () => {
    render(<AgentPanel />);
    expect(screen.getByText(/Agent Status/i)).toBeInTheDocument();
  });

  test('fetches and displays agent status', async () => {
    global.fetch = jest.fn(() =>
      Promise.resolve({
        json: () => Promise.resolve({
          ForkAlpha: 'online',
          ForkBeta: 'idle',
        }),
      })
    );

    render(<AgentPanel />);
    await waitFor(() => {
      expect(screen.getByText(/ForkAlpha/i)).toBeInTheDocument();
      expect(screen.getByText(/ForkBeta/i)).toBeInTheDocument();
    });

    global.fetch.mockRestore();
  });
});
