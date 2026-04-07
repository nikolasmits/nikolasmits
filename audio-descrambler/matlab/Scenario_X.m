Fs = 44100;
L = 5;
%t = (0:Fs*L-1)*T;
%f = Fs*(0:(l-1))/l;

% Scrambled Audio Signal
[y1, Fs1] = audioread('D:\Desktop\EEE\Yr 2\ELEC0008__Design & Professional Practice 2\Scenario X\scrambled.wav');
duration = length(y1)/Fs1;

t = (0:length(y1) - 1) / Fs;

%t1 = linspace(0, duration, length(y1));

figure();
plot(t, y1);
xlabel('Time (s)');
ylabel('Amplitude');
title('Scrambled Audio Signal in Time Domain');

Y1 = fft(y1);

%f1 = linspace(0, Fs1, length(Y1));
frequencies = linspace(0, Fs/2, length(Y1));

figure();
plot(frequencies, abs(Y1(1:length(Y1)/2)));
xlabel('Frequency (Hz)');
ylabel('Magnitude');
title('Scrambled Audio Signal in Frequency Domain');

% Original Audio Signal
[y2, Fs2] = audioread('D:\Desktop\EEE\Yr 2\ELEC0008__Design & Professional Practice 2\Scenario X\original.wav');
duration = length(y1)/Fs2;

%t2 = linspace(0, duration, length(y2));

figure();
plot(t, y2);
xlabel('Time (s)');
ylabel('Amplitude');
title('Original Audio Signal in Time Domain');

Y2 = fft(y2);

%f2 = linspace(0, Fs2, length(Y2));

figure();
plot(frequencies, abs(Y(1:length(Y2)/2)));
xlabel('Frequency (Hz)');
ylabel('Magnitude');
title('Original Audio Signal in Frequency Domain');

% Define the bandstop filter specifications
Fstop1 = 7900;   % Lower stopband frequency (Hz)
Fpass1 = 7950;   % Lower passband frequency (Hz)
Fpass2 = 8050;   % Upper passband frequency (Hz)
Fstop2 = 8100;   % Upper stopband frequency (Hz)
Astop = 60;      % Stopband attenuation (dB)
Apass = 1;       % Passband ripple (dB)

% Design the filter using a Butterworth filter
[b_bandstop, a_bandstop] = butter(4, [Fstop1 Fpass1 Fpass2 Fstop2]/(Fs/2), 'stop');

% Apply the bandstop filter
filtered_signal_bandstop = filter(b_bandstop, a_bandstop, y1);

% Generate a 7 kHz sine wave
t = (0:length(y1) - 1) / Fs;
sine_wave = sin(2 * pi * 7000 * t);

% Multiply the filtered signal by the sine wave
flipped_signal = filtered_signal_bandstop .* sine_wave';

% Define the low pass filter specifications
Fpass = 4000;    % Passband frequency (Hz)
Fstop = 4500;    % Stopband frequency (Hz)
Apass = 1;       % Passband ripple (dB)
Astop = 60;      % Stopband attenuation (dB)

% Design the filter using a Butterworth filter
[b_lowpass, a_lowpass] = butter(6, Fpass/(Fs/2), 'low');

% Apply the low pass filter
descrambled_signal = filter(b_lowpass, a_lowpass, flipped_signal);

% Play the original audio
sound(y1, Fs);
pause(length(y1) / Fs);

% Time axis
%t = (0:length(y) - 1) / Fs;

% Plot the descrambled signal in the time domain
subplot(2, 1, 2);
plot(t, descrambled_signal);
title('Descrambled Signal (Time Domain)');
xlabel('Time (s)');
ylabel('Amplitude');

% Compute the single-sided amplitude spectrum of the original and descrambled signals
Y1 = fft(y1);
Y1 = abs(Y(1:length(y1)/2 + 1));
Y1 = Y1 / max(Y1); % Normalize for better visualization

Descrambled_Y = fft(descrambled_signal);
Descrambled_Y = abs(Descrambled_Y(1:length(descrambled_signal)/2 + 1));
Descrambled_Y = Descrambled_Y / max(Descrambled_Y); % Normalize

frequencies = linspace(0, Fs/2, length(Y1));

% Plot the spectra
figure;
subplot(2, 1, 1);
plot(frequencies, 20*log10(Y1));
title('Scrambled Signal (Frequency Domain)');
xlabel('Frequency (Hz)');
ylabel('Magnitude (dB)');

subplot(2, 1, 2);
plot(frequencies, 20*log10(Descrambled_Y));
title('Descrambled Signal (Frequency Domain)');
xlabel('Frequency (Hz)');
ylabel('Magnitude (dB)');



% % Play the descrambled audio
% sound(descrambled_signal, Fs);
% 
% function Hd = Filter_8k
% 
% Fs = 44100;  % Sampling Frequency
% 
% N   = 4;     % Order
% Fc1 = 7900;
% Fc2 = 8100;
% 
% h  = fdesign.bandstop('N,F3dB1,F3dB2', N, Fc1, Fc2, Fs);
% Hd = design(h, 'butter');
% end
% 
% function Hd = lpfilter
% 
% Fs = 44100;
% 
% N  = 10;
% Fc = 5000;
% 
% h  = fdesign.lowpass('N,F3dB', N, Fc, Fs);
% Hd = design(h, 'butter');
% end