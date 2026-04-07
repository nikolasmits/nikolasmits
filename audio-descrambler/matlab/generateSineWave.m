function y = generateSineWave(amplitude, frequency, phase, numSamples)
    t = 0:(2*pi)/numSamples:(2*pi)*(1-1/numSamples); % Time vector
    y = amplitude * sin(2*pi*frequency*t + phase);
end
