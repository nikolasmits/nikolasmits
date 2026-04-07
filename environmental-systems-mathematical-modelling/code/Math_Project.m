% SECTION 1 - Load variables
clear
close all
clc
% Replace the path within quotation marks below to the folder where the
% data is stored in your computer
cd 'D:\Desktop\EEE\Mathematical Modelling and Analysis 1\Team Project\Flow Data'
FL = dir('*.csv');

% Read the spreadsheet with dates and transfom it into an array
time = readtable('Date.xlsx');
time = table2array(time);

% surface areas and volumes
A1 = 8.1925e10;                     % Superior
V01 = 12000*1E9;
A2 = 1.1685e11;                     % Mi-Huron
V02 = (3500+4900)*1E9;
A3 = 2.5404e10;                     % Erie
V03 = 480 * 1E9;
A4 = 1.9121e10;                     % Ontario
V04 = 1640 * 1E9;

% load diversions
% Terms multiplied convert data from m3/s to mm over the lakes surface area
D1 = readmatrix('D1.csv')*1000*60*60*24*30/A1;
D2 = readmatrix('D2.csv')*1000*60*60*24*30/A2;
D3 = readmatrix('D3.csv')*1000*60*60*24*30/A3;

% load connecting flows
F1 = readmatrix('Fo1.csv')*1000*60*60*24*30/A1;
F2 = readmatrix('Fo2.csv')*1000*60*60*24*30/A2;
F3 = readmatrix('Fo3.csv')*1000*60*60*24*30/A3;
F4 = readmatrix('Fo4.csv')*1000*60*60*24*30/A4;

% load evaporation
E1 = readmatrix('E1.csv');
E2 = readmatrix('E2.csv');
E3 = readmatrix('E3.csv');
E4 = readmatrix('E4.csv');

% load precipitation
P1 = readmatrix('P1.csv');
P2 = readmatrix('P2.csv');
P3 = readmatrix('P3.csv');
P4 = readmatrix('P4.csv');

% load runoff
R1 = readmatrix('R1.csv');
R2 = readmatrix('R2.csv');
R3 = readmatrix('R3.csv');
R4 = readmatrix('R4.csv');

% compute ODEs 5.1 to 5.4
% Multiplication by A_i and 1e-3 converts to m3 per month
dV1 = (  R1 + P1 + D1 - F1 - E1) * A1                       * 1E-3;
dV2 = ( (R2 + P2 - D2 - F2 - E2) * A2 +       (F1 * A1) )   * 1E-3;
dV3 = ( (R3 + P3 - D3 - F3 - E3) * A3 +       (F2 * A2) )   * 1E-3;
dV4 = ( (R4 + P4      - F4 - E4) * A4 + (D3 + F3) * A3  )   * 1E-3;

% Integration loops. Timestep = 1month
% Notice that V_i (in this case) is simply the cumulative sum of the
% differentials. For concentration solutions a Euler scheme needs to be
% implemented
V1 = zeros(size(dV1));
V2 = zeros(size(dV2));
V3 = zeros(size(dV3));
V4 = zeros(size(dV4));

for in = 1 : length(dV1)
    V1(in) = sum(dV1(1:in));
    V2(in) = sum(dV2(1:in));
    V3(in) = sum(dV3(1:in));
    V4(in) = sum(dV4(1:in));
end

clear in
V1 = V1 + V01;
V2 = V2 + V02;
V3 = V3 + V03;
V4 = V4 + V04;
%%
% t = [1:840];
% plot(time, V1, 'k-')
% grid on
% xlabel('month')
% ylabel('Total Volume (m^3)')
% hold on
% plot(time, V2, 'r-')
% plot(time, V3, 'c-')
% plot(time, V4, 'b-')

%% Pollution
m1 = zeros(size(dV1));
m2 = zeros(size(dV1));
m3_3 = zeros(size(dV1));
m4_3 = zeros(size(dV1));

%Initial Values
%kg

m1(1) = 75000 * 1E3 ;
m2(1) = 0;
m3_3(1) = 0;
m4_3(1) = 0;

%kg/m3
cir = 0;
rho1_3 = zeros(size(dV1));
rho2_3 = zeros(size(dV1));
rho3_3 = zeros(size(dV1));
rho4_3 = zeros(size(dV1));


for t = 1 : (length(dV1))
    rho1_3(t) = m1(t) / V1(t);
    rho2_3(t) = m2(t) / V2(t);
    rho3_3(t) = m3_3(t) / V3(t);
    rho4_3(t) = m4_3(t) / V4(t);

    dm1_3 = (cir * R1(t)*A1 - rho1_3(t) * F1(t)*A1)* 1E-3;
    dm2_3 = (cir * R2(t)*A2 + rho1_3(t) * F1(t)*A1 - rho2_3(t) * (F2(t) + D2(t))*A2)* 1E-3;
    dm3_3 = (cir * R3(t)*A3 + rho2_3(t) * F2(t)*A2 - rho3_3(t) * (F3(t) + D3(t))*A3)* 1E-3;
    dm4_3 = (cir * R4(t)*A4 + rho3_3(t) * (F3(t) + D3(t))*A3 - rho4_3(t) * F4(t)*A4)* 1E-3;

    m1(t+1) = m1(t) + dm1_3;
    m2(t+1) = m2(t) + dm2_3;
    m3_3(t+1) = m3_3(t) + dm3_3;
    m4_3(t+1) = m4_3(t) + dm4_3;

    dm1(t) = dm1_3;
    dm2(t) = dm2_3;
    dm3(t) = dm3_3;
    dm4(t) = dm4_3;
end
rho1_3(length(dV1)) = m1(length(dV1)) / V1(length(dV1));
rho2_3(length(dV1)) = m2(length(dV1)) / V2(length(dV1));
rho3_3(length(dV1)) = m3_3(length(dV1)) / V3(length(dV1));
rho4_3(length(dV1)) = m4_3(length(dV1)) / V4(length(dV1));
%% Critical Points

figure()
subplot(2,2,1)
plot(time, dm1, 'r-')
ylabel('Change in mass')
xlabel('Time (years)')
legend('Superior')
hold on
plot(time, zeros(size(time)), 'b-')
legend('Zero')
grid on

hold off

subplot(2,2,2)
plot(time, dm2, 'b-')
ylabel('Change in mass')
xlabel('Time (years)')
legend('Michigan-Huron')
hold on
plot(time, zeros(size(time)), 'b-')
legend('Zero')
grid on

hold off

subplot(2,2,3)
plot(time, dm3, 'c-')
ylabel('Change in mass')
xlabel('Time (years)')
legend('Erie')
hold on
plot(time, zeros(size(time)), 'b-')
legend('Zero')
grid on

hold off

subplot(2,2,4)
plot(time, dm4, 'k-')
legend('Ontario')
ylabel('Change in mass')
xlabel('Time (years)')
legend('Ontario')
hold on
plot(time, zeros(size(time)), 'b-')
legend('Zero')
grid on

 %% 75,000 metric tons of pollution in Lake Superior in 1950
figure()
subplot(2,2,1)
plot(time, rho1_3 * 1E6, 'k', 'linewidth', 2)
ylabel('conc (μg/dm^3)')
xlabel('Time (years)')
title('Superior')
legend("75000 tons")
grid on

subplot(2,2,2)
plot(time, rho2_3 * 1E6, 'b', 'linewidth', 2)
ylabel('conc (μg/dm^3)')
xlabel('Time (years)')
title('Michigan-Huron')
legend("75000 tons")
grid on

subplot(2,2,3)
plot(time, rho3_3 * 1E6, 'c', 'linewidth', 2)
ylabel('conc (μg/dm^3)')
xlabel('Time (years)')
title('Erie')
legend("75000 tons")
grid on

subplot(2,2,4)
plot(time, rho4_3 * 1E6, 'r', 'linewidth', 2)
ylabel('conc (μg/dm^3)')
xlabel('Time (years)')
title('Ontario')
legend("75000 tons")
grid on

%% 50,000 metric tons of pollution in Lake Superior in 1950

m1_3 = zeros(size(dV1));
m2_3 = zeros(size(dV1));
m3_3 = zeros(size(dV1));
m4_3 = zeros(size(dV1));

%Initial Values
%kg
m1_3(1) = 50000 * 1E3 ;
m2_3(1) = 0;
m3_3(1) = 0;
m4_3(1) = 0;

%kg/m3
cir = 0;
rho1_3 = zeros(size(dV1));
rho2_3 = zeros(size(dV1));
rho3_3 = zeros(size(dV1));
rho4_3 = zeros(size(dV1));

for t = 1 : (length(dV1) - 1)
    rho1_3(t) = m1_3(t) / V1(t);
    rho2_3(t) = m2_3(t) / V2(t);
    rho3_3(t) = m3_3(t) / V3(t);
    rho4_3(t) = m4_3(t) / V4(t);

    dm1_3 = (cir * R1(t)*A1 - rho1_3(t) * F1(t)*A1)* 1E-3;
    dm2_3 = (cir * R2(t)*A2 + rho1_3(t) * F1(t)*A1 - rho2_3(t) * (F2(t) + D2(t))*A2)* 1E-3;
    dm3_3 = (cir * R3(t)*A3 + rho2_3(t) * F2(t)*A2 - rho3_3(t) * (F3(t) + D3(t))*A3)* 1E-3;
    dm4_3 = (cir * R4(t)*A4 + rho3_3(t) * (F3(t) + D3(t))*A3 - rho4_3(t) * F4(t)*A4)* 1E-3;

    m1_3(t+1) = m1_3(t) + dm1_3;
    m2_3(t+1) = m2_3(t) + dm2_3;
    m3_3(t+1) = m3_3(t) + dm3_3;
    m4_3(t+1) = m4_3(t) + dm4_3;

end

rho1_3(length(dV1)) = m1_3(length(dV1)) / V1(length(dV1));
rho2_3(length(dV1)) = m2_3(length(dV1)) / V2(length(dV1));
rho3_3(length(dV1)) = m3_3(length(dV1)) / V3(length(dV1));
rho4_3(length(dV1)) = m4_3(length(dV1)) / V4(length(dV1));


% m1(1) = 75000 * 1E3
figure()
subplot(2,2,1)
plot(time, rho1_3 * 1E6, 'k', 'linewidth', 2)
ylabel('conc (μg/dm^3)')
xlabel('Time (years)')
title('Superior')
legend("50000 tons")
grid on

subplot(2,2,2)
plot(time, rho2_3 * 1E6, 'b', 'linewidth', 2)
ylabel('conc (μg/dm^3)')
xlabel('Time (years)')
title('Michigan-Huron')
legend("50000 tons")
grid on

subplot(2,2,3)
plot(time, rho3_3 * 1E6, 'c', 'linewidth', 2)
ylabel('conc (μg/dm^3)')
xlabel('Time (years)')
title('Erie')
legend("50000 tons")
grid on

subplot(2,2,4)
plot(time, rho4_3 * 1E6, 'r', 'linewidth', 2)
ylabel('conc (μg/dm^3)')
xlabel('Time (years)')
title('Ontario')
legend("50000 tons")
grid on


%% 25,000 metric tons of pollution in Lake Superior in 1950

m1_3 = zeros(size(dV1));
m2_3 = zeros(size(dV1));
m3_3 = zeros(size(dV1));
m4_3 = zeros(size(dV1));

%Initial Values
%kg
m1_3(1) = 25000 * 1E3 ;
m2_3(1) = 0;
m3_3(1) = 0;
m4_3(1) = 0;

%kg/m3
cir = 0;
rho1_3 = zeros(size(dV1));
rho2_3 = zeros(size(dV1));
rho3_3 = zeros(size(dV1));
rho4_3 = zeros(size(dV1));

for t = 1 : (length(dV1) - 1)
    rho1_3(t) = m1_3(t) / V1(t);
    rho2_3(t) = m2_3(t) / V2(t);
    rho3_3(t) = m3_3(t) / V3(t);
    rho4_3(t) = m4_3(t) / V4(t);

    dm1_3 = (cir * R1(t)*A1 - rho1_3(t) * F1(t)*A1)* 1E-3;
    dm2_3 = (cir * R2(t)*A2 + rho1_3(t) * F1(t)*A1 - rho2_3(t) * (F2(t) + D2(t))*A2)* 1E-3;
    dm3_3 = (cir * R3(t)*A3 + rho2_3(t) * F2(t)*A2 - rho3_3(t) * (F3(t) + D3(t))*A3)* 1E-3;
    dm4_3 = (cir * R4(t)*A4 + rho3_3(t) * (F3(t) + D3(t))*A3 - rho4_3(t) * F4(t)*A4)* 1E-3;

    m1_3(t+1) = m1_3(t) + dm1_3;
    m2_3(t+1) = m2_3(t) + dm2_3;
    m3_3(t+1) = m3_3(t) + dm3_3;
    m4_3(t+1) = m4_3(t) + dm4_3;

end

rho1_3(length(dV1)) = m1_3(length(dV1)) / V1(length(dV1));
rho2_3(length(dV1)) = m2_3(length(dV1)) / V2(length(dV1));
rho3_3(length(dV1)) = m3_3(length(dV1)) / V3(length(dV1));
rho4_3(length(dV1)) = m4_3(length(dV1)) / V4(length(dV1));


% m1(1) = 25000 * 1E3
figure()
subplot(2,2,1)
plot(time, rho1_3 * 1E6, 'k', 'linewidth', 2)
ylabel('conc (μg/dm^3)')
xlabel('Time (years)')
title('Superior')
legend("25000 tons")
grid on

subplot(2,2,2)
plot(time, rho2_3 * 1E6, 'b', 'linewidth', 2)
ylabel('conc (μg/dm^3)')
xlabel('Time (years)')
title('Michigan-Huron')
legend("25000 tons")
grid on

subplot(2,2,3)
plot(time, rho3_3 * 1E6, 'c', 'linewidth', 2)
ylabel('conc (μg/dm^3)')
xlabel('Time (years)')
title('Erie')
legend("25000 tons")
grid on

subplot(2,2,4)
plot(time, rho4_3 * 1E6, 'r', 'linewidth', 2)
ylabel('conc (μg/dm^3)')
xlabel('Time (years)')
title('Ontario')
legend("25000 tons")
grid on