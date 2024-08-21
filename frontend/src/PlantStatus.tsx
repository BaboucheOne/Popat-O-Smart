import React from 'react';
import { Chip, Tooltip } from '@mui/material';
import { green, red } from '@mui/material/colors';

interface PlantStatusProps {
  isConnected: boolean;
}

const PlantStatus: React.FC<PlantStatusProps> = ({ isConnected }) => {
  return (
    <Tooltip title={isConnected ? "Plant is connected" : "Plant is not connected"}>
      <Chip
        label={isConnected ? "Connected" : "Disconnected"}
        color={isConnected ? "success" : "error"}
        sx={{
          backgroundColor: isConnected ? green[500] : red[500],
          color: 'white',
          fontWeight: 'bold',
          borderRadius: '4px',
        }}
      />
    </Tooltip>
  );
};

export default PlantStatus;
