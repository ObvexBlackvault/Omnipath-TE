import React from 'react';

const SVGTerminalOverlay = () => { return ( <svg width="100%" height="100%" viewBox="0 0 800 600" className="absolute top-0 left-0 z-0"> <defs> <linearGradient id="glow" x1="0" y1="0" x2="1" y2="1"> <stop offset="0%" stopColor="#0ff" /> <stop offset="100%" stopColor="#00f" /> </linearGradient> <filter id="flicker"> <feTurbulence type="fractalNoise" baseFrequency="0.8" numOctaves="2" result="noise" /> <feDisplacementMap in="SourceGraphic" in2="noise" scale="1" /> </filter> </defs>

<g filter="url(#flicker)">
    <text x="20" y="40" fill="url(#glow)" fontSize="24" fontFamily="monospace">
      OMNIPATH LIVE FEED
    </text>
    <rect x="15" y="60" width="770" height="500" stroke="#0ff" strokeWidth="2" fill="none" rx="12" />
    <text x="30" y="100" fontSize="16" fill="#0f0" fontFamily="monospace">
      Awaiting command...
    </text>
  </g>
</svg>

); };

export default SVGTerminalOverlay;


