using System.Net.Http.Headers;
using System.Text.Json;

namespace Demo.PowerPlatform.Integration;

public sealed class ExternalApiClient
{
    private readonly HttpClient _httpClient;

    public ExternalApiClient(HttpClient httpClient) => _httpClient = httpClient;

    public async Task<TResponse> GetAsync<TResponse>(
        Uri endpoint,
        string bearerToken,
        string correlationId,
        CancellationToken cancellationToken)
    {
        if (endpoint.Scheme != Uri.UriSchemeHttps)
            throw new InvalidOperationException("External integrations must use HTTPS.");

        using var request = new HttpRequestMessage(HttpMethod.Get, endpoint);
        request.Headers.Authorization = new AuthenticationHeaderValue("Bearer", bearerToken);
        request.Headers.Add("x-correlation-id", correlationId);

        using var response = await _httpClient.SendAsync(request, cancellationToken);
        if (!response.IsSuccessStatusCode)
            throw new ExternalIntegrationException((int)response.StatusCode, correlationId);

        await using var stream = await response.Content.ReadAsStreamAsync(cancellationToken);
        return await JsonSerializer.DeserializeAsync<TResponse>(stream, cancellationToken: cancellationToken)
            ?? throw new ExternalIntegrationException(502, correlationId);
    }
}

public sealed class ExternalIntegrationException : Exception
{
    public int StatusCode { get; }
    public string CorrelationId { get; }

    public ExternalIntegrationException(int statusCode, string correlationId)
        : base($"External integration failed. Correlation ID: {correlationId}")
    {
        StatusCode = statusCode;
        CorrelationId = correlationId;
    }
}
