using System.Net.Http.Headers;
using System.Text;
using System.Text.Json;

namespace Demo.PowerPlatform.Integration;

public sealed class SecureServiceGateway
{
    private readonly HttpClient _httpClient;
    private readonly HashSet<string> _allowedHosts;

    public SecureServiceGateway(HttpClient httpClient, IEnumerable<string> allowedHosts)
    {
        _httpClient = httpClient;
        _allowedHosts = new HashSet<string>(allowedHosts, StringComparer.OrdinalIgnoreCase);
    }

    public async Task<string> PostJsonAsync(Uri endpoint, string accessToken, object payload, CancellationToken cancellationToken)
    {
        ValidateEndpoint(endpoint);

        using var request = new HttpRequestMessage(HttpMethod.Post, endpoint);
        request.Headers.Authorization = new AuthenticationHeaderValue("Bearer", accessToken);
        request.Content = new StringContent(JsonSerializer.Serialize(payload), Encoding.UTF8, "application/json");

        using var response = await _httpClient.SendAsync(request, cancellationToken);
        var body = await response.Content.ReadAsStringAsync(cancellationToken);

        if (!response.IsSuccessStatusCode)
            throw new InvalidOperationException($"External service returned {(int)response.StatusCode}.");

        return body;
    }

    private void ValidateEndpoint(Uri endpoint)
    {
        if (endpoint.Scheme != Uri.UriSchemeHttps)
            throw new InvalidOperationException("Only HTTPS endpoints are allowed.");
        if (!_allowedHosts.Contains(endpoint.Host))
            throw new InvalidOperationException("Endpoint host is not allowlisted.");
    }
}
