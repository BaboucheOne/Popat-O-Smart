import React from 'react';
import GenericCard from './GenericCard';
import DescriptionIcon from '@mui/icons-material/Description';

interface ReportCardProps {
  numberOfReports: number;
}

const ReportCard: React.FC<ReportCardProps> = ({ numberOfReports }) => {
  return (
    <GenericCard
      icon={DescriptionIcon}
      title={numberOfReports.toString()}
      subtitle="Reports"
      backgroundColor="rgba(116,192,255,0.49)"
    />
  );
};

export default ReportCard;
