z = [0:10];
P1 = 101325*(0.00043.*z+1).^(-5.25);
P2 = 101325.*exp(-(0.034/288.15).*z);
plot(z,P1,'-o');
hold on
plot(z,P2,'-o');
grid on
xlabel('Altitude (km)')
ylabel('Atmospheric Pressure (Pa)')
title('Atmospheric pressure against altitude')
legend('Constant temperature','Temperature dependent')
