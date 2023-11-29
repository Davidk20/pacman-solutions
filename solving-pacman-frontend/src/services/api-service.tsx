import { config } from "../constants";

/**
 * Service handling the connection between the frontend and backend applications.
 */

/**
 * Fetch an overview of all available levels.
 * @returns A list containing the available levels.
 */
export async function fetchOverview(): Promise<string[]> {
  const api_url = config.url.API_URL;
  const queryUrl = `${api_url}/get-levels`;
  const response = await fetch(queryUrl);
  return response.json();
}


/**
 * Fetch a single level, provided the level number.
 * @param levelNum The level being requested.
 */
export async function fetchLevel(levelNum: number): Promise<Array<Array<number>>> {
  const api_url = config.url.API_URL;
  const queryUrl = `${api_url}/get-board?level_num=${levelNum}`;
  const response = await fetch(queryUrl);
  return response.json();
}
