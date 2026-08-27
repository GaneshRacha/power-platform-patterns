using System.Net.Http.Headers;
using System.Text;
using System.Text.Json;

namespace Demo.PowerPlatform.Integration;

/// <summary>OAuth Client-Credential Token Service — Reusable OAuth Client-Credential Token Service engineering pattern.</summary>
public sealed class OauthClientCredentialTokenServiceClient
{
    private readonly HttpClient _client;
    public OauthClientCredentialTokenServiceClient(HttpClient client) => _client = client;

    public async Task<string> SendAsync(Uri endpoint, string token, object payload, CancellationToken cancellationToken)
    {
        if (endpoint.Scheme != Uri.UriSchemeHttps)
            throw new InvalidOperationException("HTTPS is required.");

        using var request = new HttpRequestMessage(HttpMethod.Post, endpoint);
        request.Headers.Authorization = new AuthenticationHeaderValue("Bearer", token);
        request.Headers.Add("x-correlation-id", Guid.NewGuid().ToString("N"));
        request.Content = new StringContent(JsonSerializer.Serialize(payload), Encoding.UTF8, "application/json");

        using var response = await _client.SendAsync(request, cancellationToken);
        var body = await response.Content.ReadAsStringAsync(cancellationToken);
        if (!response.IsSuccessStatusCode)
            throw new InvalidOperationException($"Integration failed with HTTP {(int)response.StatusCode}.");
        return body;
    }
}
