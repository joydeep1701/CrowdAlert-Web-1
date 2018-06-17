import {
  MAP_UPDATE_CENTER,
  MAP_UPDATE_ZOOM,
} from './actionTypes';

const initialState = {
  isVisible: false,
  lat: 0,
  lng: 0,
  zoom: 4,
};

function mapUpdateReducer(state = initialState, action) {
  switch (action.type) {
    case MAP_UPDATE_CENTER:
      if (action.payload.lat && action.payload.lng) {
        return {
          ...state,
          lat: action.payload.lat,
          lng: action.payload.lng,
        };
      }
      break;
    case MAP_UPDATE_ZOOM:
      if (action.payload.zoom) {
        return {
          ...state,
          zoom: action.payload.zoom,
        };
      }
      break;
    default:
      break;
  }
  return state;
}

export default mapUpdateReducer;
