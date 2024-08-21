import React from 'react';
import { Box, Card, CardContent, Typography } from '@mui/material';

interface GenericCardProps {
  icon: React.ElementType;
  title: string;
  subtitle: string;
  backgroundColor: string;
}

const GenericCard: React.FC<GenericCardProps> = ({ icon: Icon, title, subtitle, backgroundColor }) => (
  <Box style={{ boxShadow: '0 4px 8px rgba(0, 0, 0, 0.2)' }} sx={{ minWidth: 250 }}>
    <Card variant="outlined">
      <CardContent style={{ backgroundColor }}>
        <Icon style={{ fontSize: 30 }} />
        <Typography variant="h5" component="div">
          {title}
        </Typography>
        <Typography sx={{ fontSize: 14 }} color="text.secondary" gutterBottom>
          {subtitle}
        </Typography>
      </CardContent>
    </Card>
  </Box>
);

export default GenericCard;
