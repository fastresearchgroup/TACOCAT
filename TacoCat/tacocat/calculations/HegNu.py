#Lane Carasik
#Last Modified: 12/15/2015

'''% if Pe <= 200
%     Nu = 24.15*log10(-8.12 + 12.76*PtoD - 3.65*PtoD^2);
% else if Pe > 200
%         Nu = 24.15*log10(-8.12 + 12.76*PtoD - 3.65*PtoD^2) ...
%             + 0.0174*(1-exp(-6*(PtoD-1)))*(Pe-200)^0.9;
%     end
% end'''

import numpy as np

def Nu(PtoD,Pe):
	if Pe <= 150:
		Nu = 4.496*(-16.15 + 24.96*PtoD - 8.55*(PtoD**2))
	else:
		Nu = 4.496*(-16.15 + 24.96*PtoD - 8.55*(PtoD**2))*(Pe/150)**0.3
	return Nu