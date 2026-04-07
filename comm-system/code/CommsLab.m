/
%(https://github.com/nikolasmits/nikolasmits/tree/main/sentiment-analysis) ¨’úíóp[=]\Define an alphabet

+/
bnary_unipolar_alphabet = [0, 1];
binary_polar_alphabet = [-1, 1];
quaternary_alphabet = [-3, -1, 1, 3];

% Generate a random bit stream
num_bits = 12;  % Should be a multiple of log2(length(alphabet))
tx_bits = randi([0, 1], 1, num_bits);

% Map the bit stream to the symbol stream using reshape
tx_symbols_binary_unipolar = map(tx_bits, binary_unipolar_alphabet);
tx_symbols_binary_polar = map(tx_bits, binary_polar_alphabet);
tx_symbols_quaternary = map(tx_bits, quaternary_alphabet);

% Display the results
disp('Bit Stream:');
disp(tx_bits);

disp('Symbol Stream (Binary Unipolar):');
disp(tx_symbols_binary_unipolar);
disp('Symbol Stream (Binary Polar):');
disp(tx_symbols_binary_polar);
disp('Symbol Stream (Quaternary):');
disp(tx_symbols_quaternary);

function tx_symbols = map(tx_bits, alphabet)
    num_symbols = length(tx_bits) / log2(length(alphabet));
    
    % Reshape the bit stream into a matrix
    bit_matrix = reshape(tx_bits, log2(length(alphabet)), num_symbols)';
    
    % Initialize the symbol stream
    tx_symbols = zeros(1, num_symbols*log2(length(alphabet)));
    
    % Map each row of the matrix to a symbol using the specified alphabet
    for k = 1:num_symbols
        tx_symbols(k) = alphabet(bi2de(bit_matrix(k, :)) + 1);
    end
end